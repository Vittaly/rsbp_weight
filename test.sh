#bash
cnt=20
for i in $(eval echo {1..$cnt}); do echo 10 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 11 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 3.01 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 3.02 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 2.99 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 3 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 1 kg > /tmp/ttyS101; sleep .3; echo $i;  done
for i in $(eval echo {1..$cnt}); do echo 14 kg > /tmp/ttyS101; sleep .3; echo $i;  done