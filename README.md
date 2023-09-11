# python clean up old files in s3
![made-with-python][made-with-python]
![Python Versions][pyversion-button]

[pyversion-button]: https://img.shields.io/pypi/pyversions/Markdown.svg
[made-with-python]: https://img.shields.io/badge/Made%20with-Python-1f425f.svg

# how to use?
- configure 's3 bucketname', 'slack webhook', 'check_days variables'.
- and run


# preview
```bash
*** s3_file_clean_up ***
- buddy2
- 2023-06-27 08:42:02.303872
[+] run date: 2023-06-27
[+] cut off : 2023-06-19
---> cleaning up 8 days ago
---> scanned (37) files

[+] result
---> clean up success: 37 files
---> clean up failure: 0 files
---> total files: 37 files

1, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-10/buddy2_node.js.tar.gz
2, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-10/buddy2_node.js.tar.gz.md
3, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-10/buddy2_sql.tar.gz
4, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-10/buddy2_sql.tar.gz.md
5, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-11/buddy2_node.js.tar.gz
6, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-11/buddy2_node.js.tar.gz.md
7, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-11/buddy2_sql.tar.gz
8, [success], s3://mywebapp.log/20230612/log_export/com.main.web/2023-06-11/buddy2_sql.tar.gz.md
9, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-01/buddy2_node.js.tar.gz
10, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-01/buddy2_node.js.tar.gz.md
11, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-01/buddy2_sql.tar.gz
12, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-01/buddy2_sql.tar.gz.md
13, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-02/buddy2_node.js.tar.gz
14, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-02/buddy2_node.js.tar.gz.md
15, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-02/buddy2_sql.tar.gz
16, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-02/buddy2_sql.tar.gz.md
17, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-03/buddy2_node.js.tar.gz
18, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-03/buddy2_node.js.tar.gz.md
19, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-03/buddy2_sql.tar.gz
20, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-03/buddy2_sql.tar.gz.md
21, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-04/buddy2_node.js.tar.gz
22, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-04/buddy2_node.js.tar.gz.md
23, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-04/buddy2_sql.tar.gz
24, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-04/buddy2_sql.tar.gz.md
25, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-05/buddy2_node.js.tar.gz
26, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-05/buddy2_node.js.tar.gz.md
27, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-05/buddy2_sql.tar.gz
28, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-05/buddy2_sql.tar.gz.md
29, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-06/buddy2_node.js.tar.gz
30, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-06/buddy2_node.js.tar.gz.md
31, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-06/buddy2_sql.tar.gz
32, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-06/buddy2_sql.tar.gz.md
33, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-07/buddy2_node.js.tar.gz
34, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-07/buddy2_node.js.tar.gz.md
35, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-07/buddy2_sql.tar.gz
36, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-07/buddy2_sql.tar.gz.md
37, [success], s3://mywebapp.log/20230613/log_export/com.main.web/2023-06-08/buddy2_node.js.tar.gz
```
