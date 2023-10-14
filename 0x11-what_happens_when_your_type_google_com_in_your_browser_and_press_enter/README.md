0x11. What happens when you type google.com in your browser and press Enter
DevOps	Network	SysAdmin

# Background Context
Being a Full-Stack Software Engineer means you’re comfortable interacting with any layer of the stack.

A way to easily assess this is to simply ask an engineer to explain how a software system works. They can have a general overview of the flow or can choose to dig deep in a certain area.

Let’s practice by exploring the infrastructure side (network, servers, security…) of the question.

# Introduction
Google, as we all know, is one of the most popular search engines on the web, and when we type https://www.google.com into our browser, a lot of things happen in the background that we may not be aware of. In this blog post, I will go over the numerous steps needed in getting to Google's website, and what happens in the background.

# Step 1: Domain Name System (DNS) Request
To gain access to Google's website, first, resolve the domain name to an IP address. When we enter https://www.google.com into our browser, our computer sends a DNS request to a DNS server, which returns the IP address associated with the domain name. The DNS server answers with an IP address, which the browser can use to create a connection with Google's servers.

# Step 2: Transmission Control Protocol/Internet Protocol (TCP/IP)
After obtaining the IP address of the Google server, the browser starts a TCP/IP connection with the server. This is a network protocol that is used to send data over the internet. The HTTP protocol, which is the standard protocol for communicating between web servers and clients, is utilized by the browser to submit a request to the server.

# Step 3: Firewall
The request must first travel through the firewall before reaching the Google server. A firewall is a network security device that monitors and regulates incoming and outgoing traffic based on predetermined security rules. If the request passes the security criteria, the firewall verifies whether it is approved and permits it to flow through to the Google server.

# step 4: Hypertext Transfer Protocol Secure/Secure Sockets layer (HTTPS/SSL)
The HTTPS protocol encrypts data sent between the browser and the server using SSL (Secure Sockets Layer). SSL is a cryptographic technology that ensures data transmission is safe and that it cannot be intercepted by a third party. When the browser sends a request to the server, the server returns a digital certificate with a public key. The browser encrypts the data it sends to the server using this public key.

# Step 5: Load-balancer
When a request reaches Google's servers, it is routed through a load balancer. A Load balancer, as the name suggests distributes incoming network traffic among numerous servers so that no single server becomes overburdened. In addition, the load balancer determines which server should handle the request using various techniques.

# Step 6: Google's Web Server
The request is delivered to a web server once it has been load-balanced. The web server is in charge of processing the request and returning a response. In the case of Google's website, the web server will generate an HTML page with the search results for your query (whatever you typed on the browser - https://www.google.com).

# Step 7: Google's Application Server
Google offers an application server that handles more complicated activities, such as search queries, in addition to the web server. The application server is in charge of processing the search query and returning a result to the web server. This response is then incorporated into the HTML page that the web server generates and sends back to the browser.

# Step 8: Google's Database and the Response
The last stage in gaining access to Google's website is retrieving data from the database. Google has a large database with information on billions of websites. When a user types a search query, the application server retrieves and delivers the relevant data from the database to the web server. The data is subsequently formatted by the web server into an HTML page and returned to the browser.

# Conclusion
Finally, when we type https://www.google.com into our browser and hit enter, multiple procedures happen in the background that we may be unaware of. Each stage, from resolving the domain name to obtaining data from the database, is critical to ensuring that we can visit Google's website swiftly and securely. Understanding the numerous processes involved in accessing a website is an important aspect of a software engineer's knowledge, and each stage may be adjusted to improve a website's overall performance and security.
