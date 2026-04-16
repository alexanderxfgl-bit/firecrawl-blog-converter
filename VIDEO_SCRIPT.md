# Firecrawl Blog Converter - Video Demonstration Script

## Video Overview
This video will demonstrate the Firecrawl Blog Converter, a Python tool that converts blog posts to clean markdown using the Firecrawl SDK.

## Video Duration
- Target: 3-5 minutes
- Format: Screen recording with voice narration

## Video Script

### Introduction (0:00-0:30)
```
[Screen: Show logo and title]

"Hello everyone! Today I'm going to show you the Firecrawl Blog Converter - a powerful Python tool that converts any blog post URL to clean markdown format using the Firecrawl SDK.

This tool is perfect for content creators, researchers, developers, or anyone who needs to convert web content to markdown quickly and efficiently.

Let me walk you through how it works and what you can do with it."
```

### Installation Setup (0:30-1:00)
```
[Screen: Show terminal with project setup]

"First, let's get started with the installation. Clone the repository from GitHub:

git clone https://github.com/alexanderxfgl-bit/firecrawl-blog-converter

Navigate to the project directory and install the dependencies:

cd firecrawl-blog-converter
uv pip install -r requirements.txt

You'll also need to set up your Firecrawl API key. Get yours from the Firecrawl dashboard and set it as an environment variable:

export FIRECRAWL_API_KEY='your-api-key-here'

Or create a .env file with your API key."
```

### Basic Usage Demonstration (1:00-2:30)
```
[Screen: Show command line usage]

"Let's start with basic usage. The tool has a simple command-line interface:

python blog_converter.py -u "URL" 

For example, let's convert this tech blog post:

python blog_converter.py -u "https://tech.example.com/blog-post"

You can also specify the output directory:

python blog_converter.py -u "https://tech.example.com/blog-post" -o "converted_posts"

Or change the output format to plain text:

python blog_converter.py -u "https://tech.example.com/blog-post" -f "text"

[Screen: Show the conversion process running]

Watch how it quickly scrapes the blog post and converts it to clean markdown. The tool handles all the complexity of web scraping behind the scenes."
```

### Output Examples (2:30-3:30)
```
[Screen: Show the generated markdown file]

"Here's what the output looks like. The tool creates beautifully formatted markdown with:

- A header with metadata about the original URL
- Clean, readable markdown content
- Proper formatting preserved from the original blog post

The output is ready to use in any markdown editor or documentation system.

[Screen: Show different output formats]

You can see how the tool handles different types of content - articles, blog posts, news stories - and converts them consistently to markdown format."
```

### Advanced Features (3:30-4:15)
```
[Screen: Show advanced options and batch processing]

"The tool also supports advanced features:

Custom scrape options using JSON:
python blog_converter.py -u "URL" -s '{"waitFor": 2000, "onlyMainContent": true}'

Batch processing for multiple URLs:
Use the examples/batch_converter.py script to process multiple URLs at once.

The tool handles rate limiting, error handling, and provides detailed feedback about the conversion process."
```

### Conclusion and Next Steps (4:15-5:00)
```
[Screen: Show GitHub repository and links]

"So there you have it! The Firecrawl Blog Converter - a fast, reliable tool for converting blog posts to markdown.

Key features:
- ✅ Convert any blog post URL to markdown
- ✅ Customizable output options
- ✅ Batch processing support
- ✅ Error handling and retry logic
- ✅ Clean, human-readable output

The project is open source and available on GitHub. Feel free to contribute, create issues, or submit your own examples.

If you found this tool useful, give it a star on GitHub and share it with others who might need it.

Thanks for watching, and happy converting!"
```

## Recording Tips

1. **Screen Recording**: Use OBS or similar software to record the screen
2. **Voice Over**: Record clear narration explaining each step
3. **Visual Polish**: Add smooth transitions and highlights
4. **Real Examples**: Use actual blog post URLs for the demonstration
5. **Error Handling**: Show what happens when things go wrong (e.g., invalid URLs)

## Submission Checklist

For the GitHub bounty submission, include:

- [ ] Link to this video demonstration
- [ ] Link to the GitHub repository
- [ ] Buy Me a Coffee link
- [ ] Any social media posts (optional)

## Contact Information

For questions about this video or the project:
- GitHub: alexanderxfgl-bit/firecrawl-blog-converter
- Contact: eric@firecrawl.com (for bounty-related questions)