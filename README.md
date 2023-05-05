 Traceroute Shared Links
Traceroute Shared Links is a Python application that uses the traceroute (or tracert on Windows) command to find the shared links between multiple traceroute responses. The application runs a user-specified number of traceroutes to a provided hostname and displays the shared links in the output. Additionally, the program shows the real-time tracing process as it runs.

Requirements

•	Python 3.6 or higher

•	tkinter (usually comes pre-installed with Python)

Installation

1.	Clone this repository or download the source code.
2.	Navigate to the directory containing the source code in your terminal or command prompt.

Usage

1.	Run the Python script using the following command:

python traceroute_shared_links.py 

2.	Enter the hostname (e.g., example.com) and the number of traceroutes you want to perform.

3.	Click the "Submit" button to start the traceroutes.

4.	The real-time traceroute output will be displayed in the text area of the application window.

5.	After all traceroutes are completed, a message box will show the shared links between the traceroute responses.

Notes

•	This application uses the traceroute command on Unix-based systems (Linux, macOS) and the tracert command on Windows.

•	Realtime output may vary depending on the system's responsiveness and network conditions.
