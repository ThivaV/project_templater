import os
import shutil


# Example usage:
# source_directory = '/mnt/d/TEST/x100'
# source_directory = '/mnt/d/vault/devhub/BACKUO/imgs-copy/x100_small'
source_directory = '/mnt/d/vault/devhub/BACKUO/imgs-copy/x300_medium'

# destination_directory = '/mnt/d/TEST/x100-Copy'
# destination_directory = '/mnt/d/vault/devhub/zalando_fashionista_dataset/data/processed_data/v1.0/imgs/x100_small'
destination_directory = '/mnt/d/vault/devhub/zalando_fashionista_dataset/data/processed_data/v1.0/imgs/x300_medium'

batch_size = 20000

def move_directories_in_batches(source_dir, destination_dir, batch_size):
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    
    # Initialize a counter for directories
    count = 0

    # Walk through the source directory
    for root, dirs, files in os.walk(source_dir):
        for dir_name in dirs:
            # Construct full source and destination paths
            src_path = os.path.join(root, dir_name)
            dst_path = os.path.join(destination_dir, dir_name)
            
            print(f'Moving {src_path} to {dst_path}')
            shutil.move(src_path, dst_path)
            
            count += 1
            
            # When batch_size is reached, reset counter and continue
            if count >= batch_size:
                count = 0
                break

        # To avoid descending into subdirectories
        break
        
    print('All batches processed.')

move_directories_in_batches(source_directory, destination_directory, batch_size)
