# The pixels in the input image are represented as integers.
# The algorithm distorts the input image in the following way:
# Every pixel x in the output image has a value equal to
# the average value of the pixel values from the 3 × 3 square that has its center at x
# including x itself. All the pixels on the border of x are then removed.

# Return the blurred image as an integer, with the fractions rounded down.
def boxBlur(image):
    height = len(image)
    width = len(image[0])
    print("height: " + str(height))
    print("width: " + str(width))
    result = []
    final = []
    for i in range(0, height - 2):
        for j in range(0, width - 2):

            result.append(three_by_three(i, j, image))
    
    result_h = height - 2
    result_w = width - 2

    for i in range(result_h):
        final.append(result[:result_w])
        result = result[result_w:]
    return final


def three_by_three(h_start, w_start, image):
    three_sqr_val = 0
    total_pixels = 9
    for i in range(h_start, h_start + 3):
        for j in range(w_start, w_start + 3):
            
            three_sqr_val += image[i][j]
    return(three_sqr_val // total_pixels)