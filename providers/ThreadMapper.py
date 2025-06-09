DELIMITER = ':'
class ThreadMapper:
    @staticmethod
    def map_new_thread(user_specified_id, platform_generated_id):
        with open('ThreadMappings.txt', 'a') as f:
            f.write(f'{user_specified_id}{DELIMITER}{platform_generated_id}\n')

    @staticmethod
    def get_thread_map():
        thread_map = {}
        with open('ThreadMappings.txt', 'r') as f:
            for line in f:
                user_specified_id, platform_generated_id = line.strip().split(DELIMITER)
                thread_map[user_specified_id] = platform_generated_id
        return thread_map
