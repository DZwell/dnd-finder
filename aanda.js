const puppeteer = require('puppeteer')
const screenshot = 'github.png';
(async () => {
  const browser = await puppeteer.launch({headless: true})
  const page = await browser.newPage()
  console.log(`Navigating to ${process.env.SITE}`);
  await page.goto(process.env.SITE)
  await page.type('#UserName', process.env.USERNAME)
  await page.type('#Password', process.env.PASSWORD)
  await page.click('[name="Submit"]')
  await page.waitForNavigation()
  await page.waitForSelector('#SearchItemcodeSidebar')
  await page.type('#SearchItemcodeSidebar', process.argv[2]);
  await page.click('[name="Go"]')
  await page.waitForNavigation()
  await page.screenshot({ path: screenshot })
  // await page.evaluate(() => {
  //   const el = document.getElementById('SearchItemcodeSidebar');
  //   console.log(el);
  // })
  // await page.evaluate((() => {
  //   const el = document.getElementsByClassName('.GridListing_StockIndicatorColumn GridListing_StockIndicatorColumnE');
  //   console.log(el);
  // }))
  browser.close()
  console.log('Done');
})()