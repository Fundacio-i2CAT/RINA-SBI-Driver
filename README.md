# Short description
RINA Southbound Driver is a python-based library to enable SDN controllers manage RINA-based devices. 

# Pre-requisites
<ul>
    <li> Python 3.6 or higher.</li> 
    <li> RINA implementation for OS/Linux [IRATI open source](https://https://github.com/IRATI/stack).</li> 
</ul>

# Installation

The repository contains the rina wheel in the dist folder that must be downloaded for be installed.
To install the wheel use pip:

```
pip install rina-0.0.3-py3-none-any.whl
```


# Architecture

The RINA SBI driver can be used to add functionalities to SDN controller based on Ryu Framework for controlling RINA devices. The following figure shows the SDN architecture with the RINA SBI driver. The RINA SBI driver depends on the RINA manager application that is available on the [IRATI open source](https://https://github.com/IRATI/stack).
![alt text](SDN_Controller.png)


# Source
This code has been developed within the research project TERMINET. This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 957406.

# Copyright
This code has been developed by Fundació Privada Internet i Innovació Digital a Catalunya (i2CAT).
i2CAT is a *non-profit research and innovation centre* that  promotes mission-driven knowledge to solve business challenges, co-create solutions with a transformative impact, empower citizens through open and participative digital social innovation with territorial capillarity, and promote pioneering and strategic initiatives.
i2CAT *aims to transfer* research project results to private companies in order to create social and economic impact via the out-licensing of intellectual property and the creation of spin-offs.
Find more information of i2CAT projects and IP rights at https://i2cat.net/tech-transfer/


# License
This code is licensed under the terms *Affero GPL v3*. Information about the license can be located at https://www.gnu.org/licenses/agpl-3.0.en.html.




