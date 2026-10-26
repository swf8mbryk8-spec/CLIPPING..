from unittest.mock import MagicMock
from shorts_generator.layout_spec import LayoutSpec

def test_num_clips_transmission():
    print("Testing clip count transmission...")
    for count in [5, 10, 15, 20]:
        spec = LayoutSpec()
        spec.num_clips = count
        spec.validate()
        assert spec.num_clips == count, f"Expected {count}, got {spec.num_clips}"
        print(f"Verified: {count} clips transmitted and validated.")

def test_clamping_limits():
    print("Testing clamping limits...")
    # Test valid
    spec = LayoutSpec()
    spec.num_clips = 50
    spec.validate()
    # 50 is clamped to 50 (based on my previous edit)
    assert spec.num_clips == 50, f"Expected 50, got {spec.num_clips}"

    # Test low
    spec.num_clips = 0
    spec.validate()
    assert spec.num_clips == 1, f"Expected 1, got {spec.num_clips}"
    print("Verified: Clamping limits work.")

if __name__ == "__main__":
    test_num_clips_transmission()
    test_clamping_limits()
    print("Mock tests passed successfully.")
