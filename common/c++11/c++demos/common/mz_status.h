#ifndef  COMMON_MZ_STATUS_H_
#define  COMMON_MZ_STATUS_H_

/**
 *@brief  出错码定义
 */
typedef enum {
    kMzStatusOK = 0,   /*!<成功 */
    kMzStatusInputNullPtr = 1000,  // !< 深度库模块空指针参数
    kMzStatusInvalid,  // !< 非法参数
    kMzStatusNoSupportOpt,  // !< 不支持的操作
    kMzStatusTimeout,       // !< 超时
    kMzStatusNoMemory,      // !< 内存不足
    kMzStatusNoInit,        // !<未初始化
    kMzStatusNoSupportOption ,   // !<不支持此选项
    kMzStatusNoAchieved ,   // !< 未实现完美
    kMzStatusNoImplement,   // !< 未实现
    kMzStatusEnd
}MzStatusCode;


#endif //  ! COMMON_MZ_STATUS_H_
