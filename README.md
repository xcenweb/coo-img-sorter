# coo-img-sorter

[<u>English</u>](./README.md) | [中文](./README_zh.md)

Image sorting tool-box. You need to have `Python 3.8+` installed.

This project utilizes mathematical knowledge such as `Euclidean Distance`、`Mean Squared Error` to implement the (core) function of an image sorter.

# Installation

```shell
pip install coo-img-sorter
```

# Usage

...

# TODO

- Add more image sorting algorithms: 

  - [ ] **Peak Signal-to-Noise Ratio (PSNR)**

    Evaluate image similarity by calculating the signal-to-noise ratio between the original image and the compressed or processed image.

  - [ ] **Cosine Similarity**

    Treat images as pixel value vectors and calculate the cosine similarity between them. A cosine similarity value closer to 1 indicates that the image is more similar.

  - [ ] **Perceptual Hashing** 
  
    Measure image similarity by comparing the `Hamming distance` between hash codes

  - [ ] **Histogram Comparison**

    Evaluate image similarity by calculating the color histogram of the image and comparing the differences between the histograms.

  - [ ] **Local Feature Matching**

    Evaluate image similarity by detecting key points in the image and comparing the similarity between feature descriptors.

  - [x] **Mean Squared Error (MSE)**
    
    Calculate the average difference in pixel values between two images. A smaller MSE value indicates a more similar image.

  - [x] **Structural Similarity Index (SSIM)**

    It considers differences in brightness, contrast, and structure, and provides a comprehensive similarity score. SSIM values closer to 1 indicate a more similar image.

  - [x] **RGB**
    
    Calculate the similarity value of RGB between two sets of images using `Euclidean distance`.

- Classification speed
  - [ ] Asynchronous + multithreading