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
<p>What is a Proxy Model in Django?

In Django, a proxy model is a type of model that inherits from another model but provides additional functionalities, methods, and different behaviors. It allows developers to extend the functionality of an existing model without modifying the original model's fields or creating a separate database table. Proxy models are particularly useful when you want to have multiple types of entities inheriting from the same base model, each with its own specific behaviors and functionalities.

When creating a proxy model, there are certain properties to consider:

Inheritance: A proxy model can inherit exactly from one non-abstract model class. It cannot inherit from multiple non-abstract model classes as it would result in connections between rows in different database tables.

Abstract models: A proxy model can inherit from any number of abstract class models, allowing the incorporation of additional functionality from multiple sources.

Proxy model inheritance: The proxy model can also inherit from other proxy models that share the same non-abstract parent class. This allows for further customization and extension of the model's capabilities.

What can you do with proxy models in Django?

Modifying behavior: Proxy models allow you to change the default behavior of the model by customizing its ordering, providing a different name, or implementing other Pythonic modifications.

Customized queries: Proxy models enable you to define a customized queryset to retrieve relevant data based on specific criteria associated with the model.

Unique methods and properties: Proxy models can have their own set of methods, properties, and functions, providing unique functionality tailored to their specific purpose.

Multiple user types: You can create different types of users by inheriting from a base user model and assigning distinct functionalities to each user type. This allows for varying levels of access, authentication, and specialized operations based on user roles.

In summary, proxy models in Django offer a flexible and powerful way to extend and customize the behavior of existing models, enabling developers to create specialized entities and incorporate additional functionalities while maintaining a unified codebase.</p>
<p>That's it! You can now use FormLink to store and generate PDF files for each user, from your Django web application.</p>
