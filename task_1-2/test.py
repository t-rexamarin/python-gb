import os

sub_folders = {
                'main':
                    {
                        'settings': 'settings',
                        'mainapp': 'mainapp',
                        'adminapp': 'adminapp',
                        'authapp': 'authapp',
                        'some_folder': {
                                'some_sub_folder_1': 'some_sub_folder_1',
                                'some_file': 'some_file.file',
                                'some_sub_folder2': {
                                    'some_sub_sub_folder': 'some_sub_sub_folder',
                                    'some_file': 'some_file.file'}},
                        'some_folder2': {
                            'some_sub_folder_2': 'some_sub_folder_2',
                            'some_file2': 'some_file2.file'},
                        'some_folder3': {
                            'some_sub_folder_3': 'some_sub_folder_3',
                            'some_file2': 'some_file2.file',
                            'some_sub_folder3': {
                                'some_sub_sub_folder3': 'some_sub_sub_folder3',
                                'some_file3': 'some_file3.file'}}
                    }
                }


# print(sub_folders['main']['some_folder']['some_sub_folder2'].)
path = []
def tree_builder(tree, my_path):
    for key, value in tree.items():
        if isinstance(value, dict):
            os.mkdir(os.path.join(*my_path, key))
            my_path.append(key)
            print(my_path)
            tree_builder(value, my_path)
            my_path.remove(key)
        else:
            print('not a dict')


tree_builder(sub_folders, path)
