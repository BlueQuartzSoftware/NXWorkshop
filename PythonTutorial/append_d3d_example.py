import simplnx as nx
import shutil
from pathlib import Path

def main():
    d3d_file_path = Path('Output/append_modified.dream3d')

    # Create dream3d file

    data_structure = nx.DataStructure()

    original_data_path = nx.DataPath(['Data'])

    assert nx.CreateDataArrayFilter.execute(data_structure,
        output_array_path=original_data_path,
        numeric_type_index=nx.NumericType.int32,
        tuple_dimensions=[[10, 5, 2]],
        component_count=1,
        initialization_value_str='1',
    )

    assert nx.WriteDREAM3DFilter.execute(data_structure,
        export_file_path=d3d_file_path,
        write_xdmf_file=False,
    )

    # Create copy of original for comparison

    shutil.copy(d3d_file_path, d3d_file_path.with_stem('append_original'))

    # Create data structure to append

    new_data_structure = nx.DataStructure()

    target_path = nx.DataPath(['New Data'])

    assert nx.CreateDataArrayFilter.execute(new_data_structure,
        output_array_path=target_path,
        numeric_type_index=nx.NumericType.float32,
        tuple_dimensions=[[4, 12, 3]],
        component_count=2,
        initialization_value_str='5.2',
    )

    # Create dummy data that should not be appended

    not_appended_path = target_path.with_name('Not appended')

    assert nx.CreateDataArrayFilter.execute(new_data_structure,
        output_array_path=target_path.with_name('Not appended'),
        numeric_type_index=nx.NumericType.float32,
        tuple_dimensions=[[4, 12, 3]],
        component_count=2,
        initialization_value_str='5.2',
    )

    # Append "New Data"

    assert nx.append_to_dream3d_file(d3d_file_path, new_data_structure, target_path)

    # Verify

    result_data_structure = nx.DataStructure()

    assert nx.ReadDREAM3DFilter.execute(result_data_structure,
        import_data_object=nx.Dream3dImportParameter.ImportData(d3d_file_path),
    )

    assert result_data_structure.exists(original_data_path)
    assert result_data_structure.exists(target_path)
    assert not result_data_structure.exists(not_appended_path)


if __name__ == '__main__':
    main()
