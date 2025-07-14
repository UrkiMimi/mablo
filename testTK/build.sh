# run wine compile command
wine build.cmd

# compile into an ISO image
genisoimage -o test.iso dist
mv test.iso ~/Downloads