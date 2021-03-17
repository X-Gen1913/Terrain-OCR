# TerrainOCR
Object Detection of alphabets and digits on terrain images and videos by applying Deep learning. Export the output at regular time intervals to a spreadsheet.

## Thought process :thinking:
We thought about the problem and thought of splitting the problem into 4 parts first processing the video :video_camera: then proceesing the image :film_strip: then do the alpabhet detection :film_strip: then writing to csv.

## Hunt for the dataset
I had now started the hunt for the dataset and after 2 hours of relentless searching  :mag: we found nothing similar test data :sad: so we tried something ingenious what we did was take a some photos of the test data then add letters onto it by using a dataset of alhapbets on it by opencv by differning the weight of the sum.

## Preprocessing
Now here comes the hard part :fearful: . I had the dataset already spilt into its section but now I had to load it into an array.
Then I augmented the data use image data generator then sent it through the model.

## Model
We used our own model so we could hypertune the parameters we had accuracy of about 82 percent :smile:.


