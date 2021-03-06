from practice_4.modify_data import modify_data
from practice_4.file_controller import FileController

if __name__ == "__main__":
    file_controller = FileController()
    config = file_controller.read_file("data.json")
    config.update(modify_data)
    file_controller.write_file(config, "result.json")
