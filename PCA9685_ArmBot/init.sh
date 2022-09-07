
##################################
### On Startup
# adduser doclock17
##
# usermod -aG sudo doclock17
##
# exit
##################################
### To Access
# jupyter-lab --no-browser --port 7109
###
# ssh -NL 7109:localhost:7109 doclock17@10.0.0.109
###
# http://localhost:7109/lab
##################################

# ubuntu_init.sh
echo " "
echo "Updating . . ."
echo " "
sudo apt update
sudo apt-get update
sudo apt dist-upgrade -y --allow-downgrades
sudo apt-get dist-upgrade -y --allow-downgrades
sudo apt autoremove -y
sudo apt-get autoremove -y
echo "System Updated"
echo " "


# tools_init.sh
echo " "
echo "Installing Dependencies"
echo " "
## Install Dependency Libraries and Utilities
sudo apt-get install xsel -y
sudo apt-get install xclip -y
sudo apt-get install cmake -y
sudo apt-get install figlet -y
sudo apt-get install pv -y
sudo apt-get install curl -y
sudo apt-get install gcc -y
sudo apt-get install g++ -y
sudo apt-get install micro -y
sudo apt-get install tilix -y
sudo apt-get install net-tools -y
sudo apt-get install screen -y
sudo apt-get install htop -y
sudo apt-get install links2 -y
sudo apt-get install elinks -y
sudo apt-get install git -y
sudo apt-get install python3 -y
sudo apt-get install python3-pip -y
sudo apt-get install python3-venv -y
sudo apt-get install openjdk-8-jdk -y
sudo apt-get install openjdk-11-jdk -y
sudo apt-get install openjdk-18-jdk -y
# sudo apt-get install code -y
#sudo apt install python-is-python3 -y
echo " "
echo "Dependecies Installed"
echo " "

# jupyter_init1.sh
echo " "
echo "Installing Node"
echo " "
sudo apt-get purge nodejs npm -y
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
echo " "
echo "Node Installed"
echo " "

# jupyter_init2.sh
echo " "
echo "Installing jupyter configuration ..."
echo " "
pip install jupyter
pip install jupyterlab
pip install jupyterlab-git
#pip3 install jupyter
#pip3 install jupyterlab
#pip3 install jupyterlab-git


ip4=$(/sbin/ip -o -4 addr list eth0 | awk '{print $4}' | cut -d/ -f1)
echo ""
echo "Your ip address is: $ip4 but you will still need to tunnel to Jupyter"
dirname=$(whoami)
echo ""
echo "Your username for directory assignment is: $dirname"
echo ""

echo ""
echo "Adding virtual environment to the PATH ..."
echo ""

# Add venv to the PATH
echo """
# Add venv PATH
export PATH=/root/.local/bin:$PATH
export PATH=/home/$dirname/.local/bin:$PATH
alias python=python3
""" >> ~/.bashrc

export PATH=/root/.local/bin:$PATH
export PATH=/home/$dirname/.local/bin:$PATH




jupyter-lab --generate-config -y
echo "# My Jupyter Config: " >> /home/$dirname/.jupyter/jupyter_lab_config.py
echo "c.JupyterApp.open_browser = False" >> /home/$dirname/.jupyter/jupyter_lab_config.py
echo "c.ServerApp.allow_remote_access = True" >> /home/$dirname/.jupyter/jupyter_lab_config.py
#echo "c.ServerApp.ip = '$ip4'" >> /home/$dirname/.jupyter/jupyter_lab_config.py
echo "c.ServerApp.ip = 'localhost'" >> /home/$dirname/.jupyter/jupyter_lab_config.py
echo "c.ServerApp.port = 8888" >> /home/$dirname/.jupyter/jupyter_lab_config.py
echo "c.ServerApp.password = ''" >> /home/$dirname/.jupyter/jupyter_lab_config.py
echo "Jupyter Lab Configured"
echo " "

jupyter-notebook --generate-config -y
echo "# My Jupyter Config: " >> /home/$dirname/.jupyter/jupyter_notebook_config.py
echo "c.JupyterApp.open_browser = False" >> /home/$dirname/.jupyter/jupyter_notebook_config.py
echo "c.ServerApp.allow_remote_access = True" >> /home/$dirname/.jupyter/jupyter_notebook_config.py
#echo "c.ServerApp.ip = '$ip4'" >> /home/$dirname/.jupyter/jupyter_notebook_config.py
echo "c.ServerApp.ip = 'localhost'" >> /home/$dirname/.jupyter/jupyter_notebook_config.py
echo "c.ServerApp.port = 8888" >> /home/$dirname/.jupyter/jupyter_notebook_config.py
echo "c.ServerApp.password = ''" >> /home/$dirname/.jupyter/jupyter_notebook_config.py
echo "Jupyter Notebook Configured"

python3 -m venv venv --system-site-packages
python -m ipykernel install --user --name=venv

echo " "
echo "Script Complete!"
echo " "
echo "You should now reboot"
echo " "
echo "#sudo reboot now"
echo " "


