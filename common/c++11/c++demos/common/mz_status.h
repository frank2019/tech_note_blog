#ifndef  COMMON_MZ_STATUS_H_
#define  COMMON_MZ_STATUS_H_

/**
 *@brief  �����붨��
 */
typedef enum {
    kMzStatusOK = 0,   /*!<�ɹ� */
    kMzStatusInputNullPtr = 1000,  // !< ��ȿ�ģ���ָ�����
    kMzStatusInvalid,  // !< �Ƿ�����
    kMzStatusNoSupportOpt,  // !< ��֧�ֵĲ���
    kMzStatusTimeout,       // !< ��ʱ
    kMzStatusNoMemory,      // !< �ڴ治��
    kMzStatusNoInit,        // !<δ��ʼ��
    kMzStatusNoSupportOption ,   // !<��֧�ִ�ѡ��
    kMzStatusNoAchieved ,   // !< δʵ������
    kMzStatusNoImplement,   // !< δʵ��
    kMzStatusEnd
}MzStatusCode;


#endif //  ! COMMON_MZ_STATUS_H_
