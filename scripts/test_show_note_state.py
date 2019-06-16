import pytest
import show_note_state


def test_get_subject_info():
    filename =  '1.opencv_字符串.md'
    ret = show_note_state.get_subject_info(filename)
    assert ret is not None
    print(ret)
    assert (ret['subject_type'] == 'release') and (ret['id'] == '1')

    filename = 'todo.6.opencv_Mat初识.md'
    ret = show_note_state.get_subject_info(filename)
    assert ret is not None
    print(ret)
    assert (ret['subject_type'] == 'todo') and (ret['prority'] == '6') 

    filename = 'opencv_Mat.md'
    ret = show_note_state.get_subject_info(filename)
    assert ret is not None
    print(ret)
    assert (ret['subject_type'] == 'done') and (ret['category'] == 'opencv') 

    filename = 'opencv_Mat'
    ret = show_note_state.get_subject_info(filename)
    assert ret is  None

