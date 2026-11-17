# Test Results

Har image `samples/test_images/` se test karein aur table fill karein.

| # | Test case | Expected | Actual prediction | Confidence | Pass/Fail |
|---|-----------|----------|-------------------|-----------|-----------|
| 1 | Clear photo of a cat | Cat label, high confidence | | | |
| 2 | Clear photo of a dog | Dog breed label, high confidence | | | |
| 3 | Everyday object (laptop/mug) | Correct object label | | | |
| 4 | Blurry image | Lower confidence + warning | | | |
| 5 | Dark image | Lower confidence + warning | | | |
| 6 | Many objects in one image | Mixed labels | | | |
| 7 | Drawing / cartoon | Low confidence or wrong label | | | |
| 8 | Text image / screenshot | Low confidence or wrong label | | | |
| 9 | Object outside ImageNet classes | Wrong label, noted as limitation | | | |
| 10 | PDF upload | Clear error message | | | |
| 11 | Empty file | "File empty hai." error | | | |
| 12 | File > 5 MB | "File too large" error | | | |

## Observations
- (e.g. similar dog breeds confuse ho gaye)
