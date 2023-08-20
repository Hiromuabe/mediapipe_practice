import cv2
import mediapipe as mp

# MediaPipeのポーズコンポーネントを初期化
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# カメラの初期化
cap = cv2.VideoCapture(0)

# Poseモデルの初期化
pose = mp_pose.Pose()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # BGRからRGBへの変換
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ポーズ推定の実行
    results = pose.process(image)

    # 推定されたポーズの描画
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 結果の表示
    cv2.imshow('MediaPipe Pose', frame)

    # 'q'キーで終了
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
