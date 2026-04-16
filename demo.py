#!/usr/bin/env python3
"""
Demo script to showcase the Firecrawl Blog Converter functionality
"""

import os
import sys
sys.path.append('.')

def demo():
    """Demonstrate the blog converter functionality."""
    
    print("🚀 Firecrawl Blog Converter - Demo")
    print("=" * 40)
    
    # Check if API key is set
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        print("❌ FIRECRAWL_API_KEY environment variable not set")
        print("\nTo set up your API key:")
        print("1. Get your API key from https://firecrawl.com/dashboard")
        print("2. Run: export FIRECRAWL_API_KEY='your-api-key-here'")
        print("3. Or copy .env.example to .env and add your API key")
        return
    
    print("✅ API key found")
    
    # Test the converter with a sample URL
    test_url = "https://example.com"  # You can replace this with a real blog URL
    
    try:
        from blog_converter import convert_blog
        
        print(f"\n📄 Testing conversion with: {test_url}")
        print("⏳ Converting...")
        
        convert_blog(
            url=test_url,
            output="demo_output",
            format="markdown"
        )
        
        print("\n✅ Demo completed successfully!")
        print("Check the 'demo_output' directory for results.")
        
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        print("\nThis might be due to:")
        print("1. Invalid URL")
        print("2. Network issues")
        print("3. Rate limiting from the target website")
        print("4. API key issues")

if __name__ == '__main__':
    demo()