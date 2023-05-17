<h1>FormLink</h1>
<p>To use FormLink, you need to follow these steps:</p>
<ol>
  <li>Open the console window and run the command: <code>pip install pdfkit</code></li>
  <li>Download the wkhtmltopdf program from the website: <a href="https://wkhtmltopdf.org/downloads.html">https://wkhtmltopdf.org/downloads.html</a><br>
      <img src="./img/img1.png" alt="zdjęcie 1"></li>
  <li>Extract the downloaded file and install the program.</li>
  <li>In the bin folder, you will find configuration files needed for the application to work properly. To install the wkhtmltopdf program, copy the path of the bin folder and add it to the system environment variables on Windows:<br>
      <img src="./img/img2.png" alt="zdjęcie 2"></li>
  <li>In the Windows Settings search bar, type "Environment Variables":<br>
      <img src="./img/img3.png" alt="zdjęcie 3"></li>
  <li>Select the "Edit the system environment variables" option and click the "Environment Variables" button:<br>
      <img src="./img/img4.png" alt="zdjęcie 4"></li>
  <li>Under the "System variables" section, select the "Path" variable and click the "Edit" button:<br>
      <img src="./img/img5.png" alt="zdjęcie 5"></li>
  <li>Click the "New" button to add a new environment variable:<br>
      <img src="./img/img6.png" alt="zdjęcie 6"></li>
  <li>Enter the path you previously copied and click "OK" to save the changes:<br>
      <img src="./img/img7.png" alt="zdjęcie 7"></li>
  <li>Finally, in the views.py file, add the absolute path to the "wkhtmltopdf.exe" file on line 86:<br>
      <img src="./img/img8.png" alt="zdjęcie 8"></li>
</ol>
<p>That's it! You can now use FormLink to store and generate PDF files for each user, from your Django web application.</p>
