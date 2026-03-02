const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const url = process.env.PAGES_URL || "https://realagiorganization.github.io/blink/";
  const output = process.env.SCREENSHOT_PATH || "artifacts/pages-home.png";
  const outputDir = path.dirname(output);
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(url, { waitUntil: "networkidle", timeout: 60000 });
  await page.screenshot({ path: output, fullPage: true });
  await browser.close();
})();
