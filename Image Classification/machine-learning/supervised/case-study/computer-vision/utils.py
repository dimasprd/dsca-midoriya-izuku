"""Utility to sample cat vs dog dataset."""
import random
from pathlib import Path


def main():
    image_dir = Path("../../../data/cat_dog")
    train_dir = image_dir / "train"
    test_dir = image_dir / "test"

    dict_images = {
        "dog": [],
        "cat": [],
    }

    for file in train_dir.glob("*.jpg"):
        if file.name.split(".")[0] == "dog":
            dict_images["dog"].append(file)
        elif file.name.split(".")[0] == "cat":
            dict_images["cat"].append(file)

    for target in dict_images.keys():
        print(f"Number of {target} images:", len(dict_images[target]))

    random.seed(11)
    sample_dogs = random.sample(dict_images["dog"], 5000)
    sample_cats = random.sample(dict_images["cat"], 5000)

    print("sample dogs:", sample_dogs[:5])
    print("sample cats:", sample_cats[:5])

    target_dir = Path("../../../data/dogs_vs_cats")

    for dog in sample_dogs:
        shutil.copy2(dog, target_dir / "dog")

    for cat in sample_cats:
        shutil.copy2(cat, target_dir / "cat")


if __name__ == "__main__":
    main()
