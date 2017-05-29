# subnet-scanner-scapy

## Overview
This tool is a ***command-line subnet scanner using Scapy***.

It proceed to an ARP scan to check if each host is alive in the specified ip-range. The host-name is resolved if possible.

## Installation and Dependencies

This tool is written with **Python 2** and so require a Python 2 interpreter.

It also relies on the **Scapy** program, please visit [the official Scapy's website](http://www.secdev.org/projects/scapy/) for installation instructions.

## Usage

To show the usage and the help in the command line interface, use the ```--help``` (```-h```) option.
The ip-range has to be specified. The tool handle multiple ip-ranges (but it doesn't provides duplicate check).

Option can be specified to control the request timeout (```--timeout```, the default is 2s), the verbosity (```--quiet``` and ```--verbose```) and display preferences (```--table-results``` and ```--no-sort```).

The following list contains some usage examples :

 - ```sudo python main.py 192.168.0.*``` : scan the addresses 192.168.0.1 to 192.168.0.255.
 - ```sudo python main.py 10.2.0-1.1-7``` : scan the addresses 10.2.0.1 to 10.2.0.7 and 10.2.1.1 to 10.2.1.7.
 - ```sudo python main.py 192.168.0.* 192.168.24.165-200``` : multiple ip-range specification.
 - ```sudo python main.py -t 10 192.168.0.*``` : local subnet scan with a user-defined timeout (10s).
 - ```sudo python main.py -T 192.168.0.*``` : local subnet scan with a table display.

## Contributors

 - Etienne BOESPFLUG [etienne.boespflug@gmail.com].

## Licence

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

This tool has no license and is free to use.

## Disclaimer

This tool should only be used to discover hosts in a network.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
