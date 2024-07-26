import cv2
import mediapipe as mp
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume_range = volume.GetVolumeRange()

min_vol = volume_range[0]
max_vol = volume_range[1]

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

   
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            h, w, c = img.shape
            thumb_tip_x, thumb_tip_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            index_tip_x, index_tip_y = int(index_tip.x * w), int(index_tip.y * h)

            cv2.circle(img, (thumb_tip_x, thumb_tip_y), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (index_tip_x, index_tip_y), 10, (255, 0, 0), cv2.FILLED)

            distance = np.sqrt((thumb_tip_x - index_tip_x)**2 + (thumb_tip_y - index_tip_y)**2)

            vol = np.interp(distance, [30, 300], [min_vol, max_vol])
            volume.SetMasterVolumeLevel(vol, None)

            cv2.putText(img, f'Volume: {int(np.interp(distance, [30, 300], [0, 100]))}%', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    cv2.imshow('Volume Control', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
