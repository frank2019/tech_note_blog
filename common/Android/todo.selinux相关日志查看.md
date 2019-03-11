

使用命令

```
dmesg
```







```
[  138.353207] (1)[586:logd.auditd]type=1400 audit(1551880494.713:2949): avc: denied { write } for pid=2686 comm="ndroid.systemui" name="view_info" dev="sysfs" ino=77274 scontext=u:r:system_app:s0 tcontext=u:object_r:sysfs_hypnus:s0 tclass=file permissive=1
[  138.353228] (1)[586:logd.auditd]type=1400 audit(1551880499.223:2950): avc: denied { create } for pid=7302 comm="main" name="cgroup.procs" scontext=u:r:zygote:s0 tcontext=u:object_r:cgroup:s0 tclass=file permissive=1
[  138.443735] (6)[2557:Binder:1723_5]hypnus: No config for scene 0
[  138.743529] (0)[586:logd.auditd]type=1400 audit(1551880499.223:2950): avc: denied { create } for pid=7302 comm="main" name="cgroup.procs" scontext=u:r:zygote:s0 tcontext=u:object_r:cgroup:s0 tclass=file permissive=1
[  138.743548] (0)[586:logd.auditd]type=1400 audit(1551880499.613:2951): avc: denied { create } for pid=7348 comm="main" name="cgroup.procs" scontext=u:r:zygote:s0 tcontext=u:object_r:cgroup:s0 tclass=file permissive=1
[  138.931386] (7)[7302:c.mx6300camera2]QSEECOM: qseecom_start_app: App id 5 for [seccamfacereg64] app exists
[  138.931624] (0)[586:logd.auditd]type=1400 audit(1551880499.613:2951): avc: denied { create } for pid=7348 comm="main" name="cgroup.procs" scontext=u:r:zygote:s0 tcontext=u:object_r:cgroup:s0 tclass=file permissive=1
[  138.931643] (0)[586:logd.auditd]type=1400 audit(1551880499.803:2952): avc: denied { read write } for pid=7302 comm="c.mx6300camera2" name="mx6300_tac" dev="tmpfs" ino=14152 scontext=u:r:untrusted_app_25:s0:c512,c768 tcontext=u:object_r:mx6x_device:s0 tclass=chr_file permissive=1
[  138.931913] (0)[586:logd.auditd]type=1400 audit(1551880499.803:2952): avc: denied { read write } for pid=7302 comm="c.mx6300camera2" name="mx6300_tac" dev="tmpfs" ino=14152 scontext=u:r:untrusted_app_25:s0:c512,c768 tcontext=u:object_r:mx6x_device:s0 tclass=chr_file permissive=1
[  138.931930] (0)[586:logd.auditd]type=1400 audit(1551880499.803:2953): avc: denied { open } for pid=7302 comm="c.mx6300camera2" path="/dev/mx6300_tac" dev="tmpfs" ino=14152 scontext=u:r:untrusted_app_25:s0:c512,c768 tcontext=u:object_r:mx6x_device:s0 tclass=chr_file permissive=1
[  138.932165] (0)[586:logd.auditd]type=1400 audit(1551880499.803:2953): avc: denied { open } for pid=7302 comm="c.mx6300camera2" path="/dev/mx6300_tac" dev="tmpfs" ino=14152 scontext=u:r:untrusted_app_25:s0:c512,c768 tcontext=u:object_r:mx6x_device:s0 tclass=chr_file permissive=1
[  138.932182] (0)[586:logd.auditd]type=1400 audit(1551880499.803:2954): avc: denied { ioctl } for pid=7302 comm="c.mx6300camera2" path="/dev/mx6300_tac" dev="tmpfs" ino=14152 ioctlcmd=0x5d0a scontext=u:r:untrusted_app_25:s0:c512,c768 tcontext=u:object_r:mx6x_device:s0 tclass=chr_file permissive=1
[  138.932236] (7)[7302:c.mx6300camera2]mx6300: mx6300_tac_send_spi_cmd, response failed. rsp = -9
```







参考链接

1. [Android SELinux解析](https://blog.csdn.net/chenjinlong126/article/details/80558022)