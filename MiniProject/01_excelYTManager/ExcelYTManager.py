# ExcelYTManager using Excel file

import pandas as pd
class ExcelYTManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_excel(file_path)

    def get_video_info(self, video_id):
        video_info = self.data[self.data['video_id'] == video_id]
        if not video_info.empty:
            return video_info.to_dict(orient='records')[0]
        else:
            return None

    def add_video_info(self, video_info):
        new_row = pd.DataFrame([video_info])
        self.data = pd.concat([self.data, new_row], ignore_index=True)
        self.data.to_excel(self.file_path, index=False)

    def update_video_info(self, video_id, updated_info):
        self.data.loc[self.data['video_id'] == video_id, updated_info.keys()] = updated_info.values()
        self.data.to_excel(self.file_path, index=False)

    def delete_video_info(self, video_id):
        self.data = self.data[self.data['video_id'] != video_id]
        self.data.to_excel(self.file_path, index=False)

    def list_all_videos(self):
        return self.data.to_dict(orient='records')
    
# Example usage:
manager = ExcelYTManager('videos.xlsx')
video_info = manager.get_video_info('12345')
manager.add_video_info({'video_id': '12345', 'title': 'Sample Video', 'views': 1000})
manager.update_video_info('12345', {'title': 'Updated Video', 'views': 1500})
manager.delete_video_info('12345')
all_videos = manager.list_all_videos()