
from PIL import Image
import os
import threading

# Define a function that resizes an image
def resize_image(image_path, output_path, size):
    with Image.open(image_path) as image:
        # Resize the image
        resized_image = image.resize(size)
        # Save the resized image
        resized_image.save(output_path)

# Define a function that spawns multiple threads to resize a batch of images
def resize_images_in_batch(image_dir, output_dir, size, num_threads):
    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    # Get the paths of all image files in the input directory
    image_paths = [os.path.join(image_dir, filename) for filename in os.listdir(image_dir) if filename.endswith('.jpg')]
    # Split the image paths into num_threads chunks
    chunks = [image_paths[i:i + num_threads] for i in range(0, len(image_paths), num_threads)]
    # Spawn a thread for each chunk of image paths
    for chunk in chunks:
        threads = []
        for image_path in chunk:
            # Generate the output path for the resized image
            output_path = os.path.join(output_dir, os.path.basename(image_path))
            # Spawn a thread to resize the image
            thread = threading.Thread(target=resize_image, args=(image_path, output_path, size))
            thread.start()
            threads.append(thread)
        # Wait for all threads in the chunk to finish
        for thread in threads:
            thread.join()

# Resize a batch of images using 4 threads
resize_images_in_batch('input_dir', 'output_dir', (256, 256), 4)

