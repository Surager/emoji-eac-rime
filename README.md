# emoji-eac-rime
Convert quickphrase emoji list to rime's format.

## 使用说明

### 背景

本仓库通过 [fcitx5 quickphrase emoji](https://github.com/fcitx/fcitx5/blob/master/src/modules/quickphrase/quickphrase.d/emoji-eac.mb) 转化而来。诚然，在 rime 中通过中文映射输入 emoji 是非常高效的。但为了满足个人学习英语以及趣味打字的需求，本人亟须一个英文的 emoji 输入方案，又苦于 rime 没有提供现成的方案，故作此库。

### 使用方法

- 要使用转换好的词库，可以将本仓库中的 emoji-eac.dict.yaml 文件放到你的 rime 个人文件夹中。然后在你的 ⚠️**英文**⚠️ 词库 import_tables 中添加该词库即可。
- 要使用 python 脚本进行转换，请先下载 fcitx5 的 emoji-eac.mb，然后在同目录下运行 python 脚本即可。

## Introduction

### Background

This repo is converted from [fcitx5 quickphrase emoji](https://github.com/fcitx/fcitx5/blob/master/src/modules/quickphrase/quickphrase.d/emoji-eac.mb). Indeed, inputing emoji utilizing Chinese through rime is very efficient. However, in order to satisfy my need to learning English and happy typing, I desperately need an English emoji input solution. But rime doesn't provide such a ready-made solution. So I made this repo.

### Usage

- To use the ready-made dict, download the emoji-eac.dict.yaml file in this repo to your rime user folder. Then add this dict to your English dict import_tables. 
- To convert dict utilizing python script, please download the fcitx5's emoji-eac.mb file, then execute the python script in the same directory.

