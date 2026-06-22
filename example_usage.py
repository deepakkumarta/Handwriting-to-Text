"""
Example usage of the HandwritingToTextConverter class
Demonstrates various ways to use the OCR conversion system
"""

from handwriting_ocr import HandwritingToTextConverter
import os


def example_single_image():
    """
    Example 1: Convert a single handwritten image to text
    """
    print("=" * 60)
    print("Example 1: Single Image Conversion")
    print("=" * 60)
    print()
    
    # Initialize converter
    converter = HandwritingToTextConverter()
    
    # Path to your handwritten image (JPEG or PNG)
    image_path = "sample_handwriting.jpg"
    
    # Check if sample image exists
    if not os.path.exists(image_path):
        print(f"Note: {image_path} not found. Create a sample image first.")
        print("Expected: A JPEG/PNG image with handwritten text from Surface Laptop stylus")
        return
    
    try:
        # Convert image to text
        result = converter.convert_image_to_text(image_path)
        
        print("\nConversion Result:")
        print(f"  Input: {result['image_path']}")
        print(f"  Output: {result['output_path']}")
        print(f"  Characters extracted: {result['character_count']}")
        print("\nExtracted Text Preview:")
        print("-" * 60)
        print(result['text'][:500])  # Print first 500 characters
        if len(result['text']) > 500:
            print("...")
        print("-" * 60)
        
    except Exception as e:
        print(f"Error: {e}")


def example_custom_output():
    """
    Example 2: Convert image with custom output path
    """
    print("\n" + "=" * 60)
    print("Example 2: Custom Output Path")
    print("=" * 60)
    print()
    
    converter = HandwritingToTextConverter()
    
    image_path = "sample_handwriting.jpg"
    output_path = "converted_text.txt"
    
    if not os.path.exists(image_path):
        print(f"Note: {image_path} not found.")
        return
    
    try:
        result = converter.convert_image_to_text(image_path, output_path)
        print(f"Successfully converted and saved to: {result['output_path']}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_batch_conversion():
    """
    Example 3: Batch convert multiple images from a directory
    """
    print("\n" + "=" * 60)
    print("Example 3: Batch Conversion")
    print("=" * 60)
    print()
    
    converter = HandwritingToTextConverter()
    
    # Directory containing multiple handwritten images
    input_dir = "./handwritten_samples"
    output_dir = "./extracted_text"
    
    if not os.path.exists(input_dir):
        print(f"Note: {input_dir} directory not found.")
        print("Create a directory with multiple JPEG/PNG images to test batch conversion.")
        return
    
    try:
        results = converter.batch_convert(input_dir, output_dir)
        
        print(f"\nBatch Conversion Summary:")
        print(f"  Total images processed: {len(results)}")
        
        successful = sum(1 for r in results if 'text' in r)
        print(f"  Successful conversions: {successful}")
        print(f"  Failed conversions: {len(results) - successful}")
        
        if successful > 0:
            total_chars = sum(r.get('character_count', 0) for r in results)
            print(f"  Total characters extracted: {total_chars}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_with_preprocessing():
    """
    Example 4: Demonstrate image preprocessing
    """
    print("\n" + "=" * 60)
    print("Example 4: Image Preprocessing Demonstration")
    print("=" * 60)
    print()
    
    converter = HandwritingToTextConverter()
    
    image_path = "sample_handwriting.jpg"
    
    if not os.path.exists(image_path):
        print(f"Note: {image_path} not found.")
        return
    
    print("Image Preprocessing Steps:")
    print("1. Read image from disk")
    print("2. Convert to grayscale")
    print("3. Apply denoising filter")
    print("4. Apply binary thresholding")
    print("5. Enhance contrast using CLAHE")
    print()
    
    try:
        # Preprocess the image
        processed = converter.preprocess_image(image_path)
        print(f"✓ Preprocessing complete")
        print(f"  Processed image shape: {processed.shape}")
        print(f"  Data type: {processed.dtype}")
        print()
        print("The preprocessed image is now ready for OCR extraction.")
        
    except Exception as e:
        print(f"Error: {e}")


def example_format_validation():
    """
    Example 5: Validate image format before conversion
    """
    print("\n" + "=" * 60)
    print("Example 5: Format Validation")
    print("=" * 60)
    print()
    
    converter = HandwritingToTextConverter()
    
    test_files = [
        "image.jpg",      # Valid
        "image.jpeg",     # Valid
        "image.png",      # Valid
        "image.bmp",      # Invalid
        "image.gif",      # Invalid
        "image.tiff",     # Invalid
    ]
    
    print("Testing image format validation:\n")
    
    for filename in test_files:
        try:
            converter.validate_image_format(filename)
            print(f"✓ {filename:20} - Supported format")
        except ValueError as e:
            print(f"✗ {filename:20} - {str(e).split(':')[1].strip()}")


def main():
    """
    Run all examples
    """
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 58 + "║")
    print("║" + "  Handwriting to Text Converter - Usage Examples".center(58) + "║")
    print("║" + " " * 58 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    # Run examples
    example_single_image()
    example_custom_output()
    example_batch_conversion()
    example_with_preprocessing()
    example_format_validation()
    
    print("\n" + "=" * 60)
    print("Examples Complete")
    print("=" * 60)
    print()
    print("To use with your own images:")
    print("1. Place your JPEG/PNG handwritten images in a directory")
    print("2. Update the image_path variables in the examples")
    print("3. Run this script or use handwriting_ocr.py directly")
    print()


if __name__ == "__main__":
    main()
