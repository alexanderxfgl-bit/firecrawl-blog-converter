#!/usr/bin/env python3
"""
Batch conversion example for the Firecrawl Blog Converter
"""

import os
import sys
import json
import time
from typing import List, Dict
sys.path.append('..')

from blog_converter import convert_blog

class BatchConverter:
    """Batch blog converter for processing multiple URLs."""
    
    def __init__(self, delay: int = 2):
        self.delay = delay  # Delay between requests to avoid rate limiting
        
    def convert_urls(self, urls: List[str], output_dir: str = "batch_output", 
                    format: str = "markdown", scrape_options: str = None):
        """Convert multiple URLs to markdown files."""
        
        print(f"🚀 Starting batch conversion of {len(urls)} URLs")
        print(f"📁 Output directory: {output_dir}")
        print(f"⏱️  Delay between requests: {self.delay} seconds")
        print("-" * 50)
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        results = []
        successful = 0
        failed = 0
        
        for i, url in enumerate(urls, 1):
            print(f"\n📄 Processing URL {i}/{len(urls)}: {url}")
            
            try:
                # Convert the blog post
                convert_blog(
                    url=url,
                    output=output_dir,
                    format=format,
                    scrape_options=scrape_options
                )
                
                successful += 1
                print(f"✅ Successfully converted: {url}")
                
                # Add delay between requests
                if i < len(urls):
                    print(f"⏳ Waiting {self.delay} seconds before next request...")
                    time.sleep(self.delay)
                    
            except Exception as e:
                failed += 1
                print(f"❌ Failed to convert {url}: {e}")
                results.append({
                    'url': url,
                    'status': 'failed',
                    'error': str(e)
                })
        
        # Print summary
        print("\n" + "=" * 50)
        print("📊 BATCH CONVERSION SUMMARY")
        print("=" * 50)
        print(f"✅ Successful conversions: {successful}")
        print(f"❌ Failed conversions: {failed}")
        print(f"📈 Success rate: {successful/(successful+failed)*100:.1f}%")
        
        # Save results to JSON
        results_file = os.path.join(output_dir, "conversion_results.json")
        with open(results_file, 'w') as f:
            json.dump({
                'total_urls': len(urls),
                'successful': successful,
                'failed': failed,
                'results': results
            }, f, indent=2)
        
        print(f"\n📄 Detailed results saved to: {results_file}")
        
        return results

def main():
    """Demonstrate batch conversion functionality."""
    
    # Example list of URLs (replace with actual blog post URLs)
    test_urls = [
        "https://example.com/blog1",  # Replace with real URLs
        "https://example.com/blog2",  # Replace with real URLs  
        "https://example.com/blog3",  # Replace with real URLs
    ]
    
    # Create batch converter instance
    converter = BatchConverter(delay=3)
    
    try:
        # Convert URLs with custom options
        results = converter.convert_urls(
            urls=test_urls,
            output_dir="batch_output",
            format="markdown",
            scrape_options='{"waitFor": 2000, "onlyMainContent": true}'
        )
        
        print("\n🎉 Batch conversion completed!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Batch conversion interrupted by user")
        
    except Exception as e:
        print(f"\n❌ Error during batch conversion: {e}")
        print("\n💡 Make sure to:")
        print("1. Set your FIRECRAWL_API_KEY environment variable")
        print("2. Use valid blog post URLs")
        print("3. Check your internet connection")

if __name__ == '__main__':
    main()