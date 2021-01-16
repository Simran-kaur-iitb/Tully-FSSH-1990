import os

num_trajs=1000
num_folders=20

for i in range(num_folders):
  os.system("rm -r "+str(i))
  os.system("mkdir -p "+str(i))
  os.chdir(str(i))
  os.system("pwd")

  seed = i*i+43*i+17
  print(seed)
  os.system("echo "+str(seed)+" > seed.inp")
  os.system("echo "+str(int(num_trajs/num_folders))+" > traj.inp")

  os.system("cp ../tully .")
  os.system("cp ../sub.sh .")
  #os.system("cp ../any additional files .")
  os.system("./tully")


  os.chdir("..")
