
# Project Name: 
T24OFSDataExtractor: Streamlining T24 Data Retrieval via OFS Messages

# Overview:
T24OFSDataExtractor stands as a web-based solution catering to users interacting with Temenos T24, a vital banking software system, by harnessing the power of OFS (Open Financial Service) messages. The primary objective of this project is to simplify and automate the process of communicating with the T24 server, enabling effortless data extraction and convenient access to information residing within the T24 system.

example 1 without filter

![image](https://github.com/Mohamedallam1233/T24_dataextract/assets/52450277/db447e00-6923-4e59-bae3-31cda7758799)

and this is excel result for it 

![screen3](https://github.com/Mohamedallam1233/T24_dataextract/assets/52450277/c507d519-abbd-4762-a122-7ad86cff0d97)

example 2 with filter

![SCREEN 4](https://github.com/Mohamedallam1233/T24_dataextract/assets/52450277/042b1542-86b5-43a0-a633-983be726d63a)

and this is excel result for it 

![scrren 5](https://github.com/Mohamedallam1233/T24_dataextract/assets/52450277/9e554d2e-4996-4f08-a179-2ef23ba606cf)



# Core Functionalities:

OFS Message Generation: The web application offers an intuitive interface allowing users to select the type of request they intend to make, be it a transaction or an enquiry. Users input the necessary information, empowering the system to generate precise OFS messages tailored to their requirements.

T24 Connectivity: Leveraging Python libraries such as telnet or socket, or utilizing the "tRun tSS [ofs source]" format, the application establishes a robust connection with the T24 server. This connection facilitates the seamless transmission of OFS messages and retrieval of requested data.

Excel File Conversion: Upon successful interaction with the T24 server, the received data is efficiently converted into an Excel file format. This conversion ensures that the extracted information is presented in a structured manner, facilitating easy analysis and utilization by end-users.

# User Experience and Benefits:

Simplified Interaction: The user-friendly interface streamlines the process of interacting with T24 through OFS messages, eliminating complexities in data extraction procedures.

Data Accessibility: The tool grants users easy access to T24 data in a familiar Excel format, enhancing usability and enabling further analysis or integration into other systems.

Automation for Efficiency: By automating the communication process with T24, the application saves users' time and effort in retrieving specific datasets.

# Target Audience:

This project caters to a broad spectrum of users, including:

Bank Employees: Offering assistance in managing T24 operations efficiently.
Customers: Providing access to specific T24 data for personal or business needs.
Analysts and Developers: Facilitating data analysis and development tasks by delivering structured data in a familiar format.

# Technical Details:

The application is built using Python and Django frameworks, incorporating libraries like Paramiko for SSH connectivity. The integration of these technologies ensures secure and reliable communication with the T24 server, prioritizing data integrity and confidentiality during transmission.

# Future Enhancements:

In future iterations, the project roadmap includes the integration of visualization tools for data representation, advanced query building capabilities to empower users, and the potential implementation of automated scheduling for recurring data extraction tasks.

# Conclusion:

T24OFSDataExtractor aims to revolutionize the way users interact with T24 by simplifying data extraction via OFS messages. By offering an intuitive interface, robust connectivity, and streamlined processes, the project empowers users to effortlessly access and utilize T24 data to fulfill their diverse needs.

This comprehensive project description encapsulates the core functionalities, user benefits, target audience, technical aspects, future enhancements, and the overall impact of the T24OFSDataExtractor project. Adjustments can be made to emphasize specific details or accommodate additional aspects as needed.

# run project commands
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
