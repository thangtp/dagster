const puppeteer = require("puppeteer");

// Screenshots for:
// - hello_solid
// - hello_pipeline
// - execute_pipeline
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1680, height: 946 });

  await page.goto("http://localhost:3000/pipeline/hello_cereal_pipeline:/", {
    waitUntil: "networkidle2"
  });
  await page.screenshot({
    path: __dirname + "/hello_cereal_figure_one.png"
  });

  await page.goto("http://localhost:3000/playground/", {
    waitUntil: "networkidle2"
  });

  const [dropdownButton] = await page.$x(
    "//button[contains(., 'Select a pipeline')]"
  );
  await dropdownButton.click();

  const elements = await page.$x("//div[contains(., 'hello_cereal_pipeline')]");
  const pipelineSelection = elements[elements.length - 1];
  await pipelineSelection.click();
  await page.waitFor(1000);
  await page.screenshot({
    path: __dirname + "/hello_cereal_figure_two.png"
  });

  const [executeButton] = await page.$x(
    "//button[contains(., 'Start Execution')]"
  );

  browser.on("targetcreated", async () => {
    const [_, __, tabThree] = await browser.pages();
    await tabThree.setViewport({ width: 1680, height: 946 });
    await tabThree.waitFor(3000);
    await tabThree.screenshot({
      path: __dirname + "/hello_cereal_figure_three.png"
    });
    browser.close();
  });

  await executeButton.click();
})();

// Screenshots for:
// - hello_dag
(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  await page.setViewport({ width: 1680, height: 946 });

  await page.goto("http://localhost:3000/pipeline/hello_cereal_pipeline:/", {
    waitUntil: "networkidle2"
  });
  await page.screenshot({
    path: __dirname + "/serial_pipeline_figure_one.png"
  });

  await page.goto("http://localhost:3000/pipeline/complex_pipeline:/", {
    waitUntil: "networkidle2"
  });
  await page.screenshot({
    path: __dirname + "/complex_pipeline_figure_one.png"
  });

  browser.close();
})();
