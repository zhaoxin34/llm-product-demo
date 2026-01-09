---
name: 登录到产品
description: 当需要需要登录到产品时，使用当前SKILL
allowed-tools: Read, Bash(python:*)
---

# PDF Processing

## Quick start

Extract text:
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For form filling, see [FORMS.md](FORMS.md).
For detailed API reference, see [REFERENCE.md](REFERENCE.md).

## Requirements

Packages must be installed in your environment:
```bash
pip install pypdf pdfplumber
```


curl 'http://wolf.dev.datatist.cn/analyzer/analyzer/account/login.do' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: zh_CN' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -b 'Hm_lvt_8c2992e76f8bb7db5edf4212b4bdfee9=1767148335; HMACCOUNT=4552459EC627B28A; ANALYZER.rmbm.tmp=vP+v2/Yzdv1OCHHt2sVtQhlAUGUAIe0zGL+g6raJCppS3TfjaM2TFFwIJXt7CdKDyH5gymnqzkzUj5woR5TfVCGbKXMyPyaVUF/aE6i4U3tXwnyj0NEMhvqn6DfDpuf7z71kku20O4rh6KenHRiEVQ6tTeCWIgd9gkZQQ+EFzgNRaic3iupaYUUlkEekGHln/h91Dw308NpPa0wgFepy58AF9RP/kVxjf7nZS2zV0ZYphqTTwCnTPwJpThwdDTPikxS9MbZQ3if+WelZOUo1NYZoSCoroEgk0l0J8Rf0GZQVq2U1bsFx+/U2yVPeu0X5jHAMFj3zH5SpNKGOegRpBX66B3YeNM2Z7AOBpIZOHfZdakCwiw2vgVUP/TgpkW3FdHXry/JFREulhXFOxtnrBLFEYQikyMahzC1mx8csg0jzVgUEnEsZIm2+ETkKiu7Qf6tskxBAorkp/L6p8ovPMKytIpSia7MFW1NgAa5OfXsnJznLthRAOcjR9RYN186+gAorR5/XAq55z7tJTcCUXe8dqnaMRHZpzPWSmmlkOSs8mPegtQidMhtIlf4Pxii/vcCzIhMx0ZYrx5p7Omt52Jh/KlaHQ9D1; Hm_lpvt_8c2992e76f8bb7db5edf4212b4bdfee9=1767780100' \
  -H 'ENCRYPT-REQUEST: true' \
  -H 'Origin: http://wolf.dev.datatist.cn' \
  -H 'PROJECT-ID: 6KlTrScb8Z1mKY33' \
  -H 'Referer: http://wolf.dev.datatist.cn/aimarketer/login' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36' \
  --data-raw 'IBy5lUiSAWZ4nbOfsl/TVs2ahIAQChyAHBa+rEPRnAsLBinn4D7dCGQnf4dlpunDO2lNdjsXEzELjSmth8ZyB4WUuzcSixNXwd0VPscdtgFkLchn8rTkCOGohjvXbolj7AeaZO/hbiicvduwEnyJywbI7Lx2DsKShXX8IK4MOJA=' \
  --insecure
