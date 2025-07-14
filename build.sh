# run wine compile command
wine build.cmd

# compile into an ISO image
genisoimage -o mablo.iso dist
mv mablo.iso ~/Downloads