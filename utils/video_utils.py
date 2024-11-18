import cv2

def read_video(vide_path):
    cap = cv2.VideoCapture(vide_path)
    frames = []
    while True:
        # if cannot retrive next frame, video is done and return frames
        retrive, frame = cap.read()
        if not retrive:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames, output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    #save video as 24fps
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()
