from utils import read_video, save_video
from trackers import Tracker
from team_assigner import TeamAssigner
import cv2
def main():
    #read video
    video_frames = read_video('input_videos/08fd33_4.mp4')

    

    #init tracker
    tracker = Tracker('models/best.pt')
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path='stubs/track_stubs.pk1')

    # assign teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_colour(video_frames[0], tracks['players'][1])

    for frame_number, player_track in enumerate(tracks['players']):
        for player_id, track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_number], track['bbox'], player_id)
            tracks['players'][frame_number][player_id]['team'] = team
            tracks['players'][frame_number][player_id]['team_colour'] = team_assigner.team_colours[team]

    #draw output
    #draw object tracks
    output_video_frames = tracker.draw_annotations(video_frames,tracks)

    #save video
    save_video(output_video_frames, 'output_videos/output_video.avi')

if __name__ == '__main__':
    main()