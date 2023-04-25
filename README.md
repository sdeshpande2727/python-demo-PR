#link - https://pybuilder.io/
"# python-pybuilder-repo-structure" 

#For New REPO
  #!/bin/sh
 
AKCp1nzfsRR6kH7KJYAcGi8wZytdGuuLvHinbb7qaccuZSHzyQaKtA1Cp7KXw8eNg8iQmUpID
 
 pip install pybuilder

  If you want the bleeding edge
  (we release after every commit)
  pip install --pre pybuilder

  pyb --start-project
  pyb publish
  
  
  #For Existing repo
  
  git clone https://github.com/twentybn/GulpIO
  cd GulpIO
  python -m venv venv
  source venv/bin/activate
  pip install pybuilder

  If you want the bleeding edge
  (we release after every commit)
  pip install --pre pybuilder

  pyb


