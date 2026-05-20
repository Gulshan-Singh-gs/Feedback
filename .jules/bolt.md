## 2024-05-20 - Unoptimized Binary Assets
**Learning:** In repositories lacking automated build pipelines, large static assets like favicons are often committed unoptimized, creating massive, unnecessary network payloads for users.
**Action:** Always verify the file size of binary assets (images, fonts) in legacy or purely static frontends using `ls -la` and optimize them manually using lightweight tools like Python's `Pillow` to achieve immediate performance wins.
