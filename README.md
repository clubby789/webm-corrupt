# webm-corrupt
The WebM specification allows for videos with a length field of 0. Some players such as Discord don't handle this correctly, and the video appears to grow as the buffered ideo is assumed to be the length of the entire file.
Example: https://cdn.discordapp.com/attachments/546051174097354776/566607884335579146/time_broke.webm
