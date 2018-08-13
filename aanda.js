const puppeteer = require('puppeteer')
const screenshot = 'github.png';
const VALUES = {};

(async () => {
  const browser = await puppeteer.launch({ headless: true })
  const page = await browser.newPage()
  console.log(`Navigating to ${process.env.SITE}`);
  await page.goto(process.env.SITE)
  await page.type('#UserName', process.env.USERNAME)
  await page.type('#Password', process.env.PASSWORD)
  await page.click('[name="Submit"]')
  await page.waitForNavigation()
  await page.type('#frmItemcodeSearch', process.argv[2])
  await page.evaluate(() => {
    document.querySelector('.SubmitButton').click();
  });
  await page.waitForNavigation()
  // await page.waitForSelector('tbody');
  // VALUES.E = await page.evaluate(() => { 
  //   return document.getElementsByName('W');
  // });

  VALUES.E = await page.$eval('td .dgv-label', el => el);
    

    // document.getElementsByName('MW')[0].textContent;
    // document.getElementsByName('SW')[0].textContent;
    // document.getElementsByName('W')[0].textContent;
  await page.screenshot({path: screenshot});
  browser.close()
  console.log('Done\n');
  console.log(VALUES);
})()