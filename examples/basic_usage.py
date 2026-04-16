#!/usr/bin/env python3
"""
Basic usage example for the Firecrawl Blog Converter
"""

import os
import sys
sys.path.append('..')

from blog_converter import convert_blog

def main():
    """Demonstrate basic usage of the blog converter."""
    
    print("🚀 Firecrawl Blog Converter - Basic Usage Example")
    print("=" * 50)
    
    # Example URLs (you can replace these with actual blog posts)
    example_urls = [
        "https://example.com/blog-post",  # Replace with a real blog URL
        "https://medium.com/@example/article",  # Replace with a real article URL
    ]
    
    # Test with one URL (you'll need to provide a real URL)
    test_url = "https://example.com/blog-post"  # Change this to a real blog post URL
    
    try:
        # Convert the blog post
        convert_blog(
            url=test_url,
            output="output",
            format="markdown",
            scrape_options='{"waitFor": 2000}'
        )
        
        print(f"\n✅ Conversion completed successfully!")
        print(f"Check the 'output' directory for your converted markdown file.")
        
    except Exception as e:
        print(f"\n❌ Error during conversion: {e}")
        print("\n💡 Make sure to:")
        print("1. Set your FIRECRAWL_API_KEY environment variable")
        print("2. Use a valid blog post URL")
        print("3. Check your internet connection")

if __name__ == '__main__':
    main()