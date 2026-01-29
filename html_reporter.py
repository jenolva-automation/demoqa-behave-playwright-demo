#!/usr/bin/env python
"""
Simple HTML reporter that includes screenshots
"""
import os
import glob
from datetime import datetime

def generate_html_report():
    """Generate a simple HTML report with screenshots"""
    
    # Get all screenshots
    screenshot_files = glob.glob("screenshots/*.png")
    screenshot_files.sort()
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Behave Test Report with Screenshots</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .screenshot {{ margin: 20px 0; }}
            .screenshot img {{ max-width: 800px; border: 1px solid #ccc; }}
            .timestamp {{ color: #666; font-size: 12px; }}
            h1 {{ color: #2c3e50; }}
            .success {{ color: green; }}
            .failure {{ color: red; }}
        </style>
    </head>
    <body>
        <h1>🧪 Behave Test Report</h1>
        <p class="timestamp">Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        
        <h2>📸 Test Screenshots ({len(screenshot_files)} total)</h2>
    """
    
    for screenshot in screenshot_files:
        filename = os.path.basename(screenshot)
        html_content += f"""
        <div class="screenshot">
            <h3>{filename}</h3>
            <img src="{screenshot}" alt="{filename}">
        </div>
        """
    
    html_content += """
    </body>
    </html>
    """
    
    # Save HTML report
    with open("test_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print("📄 HTML report generated: test_report.html")

if __name__ == "__main__":
    generate_html_report()