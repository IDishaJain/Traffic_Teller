import {useDropzone} from 'react-dropzone';
import { useCallback } from 'react';
import PropTypes from 'prop-types';

export default function Dropzone({ onFileSelected }) {
  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length > 0){
      onFileSelected(acceptedFiles)
    } 
  },[onFileSelected])
  
  const {getRootProps, getInputProps, open, } = useDropzone({
    noClick: true,
    onDrop,
    accept:{
      'video/mp4': []
    }
  });

  return (
    <section className='h-full'>
      <div {...getRootProps({className: 'dropzone'})} className='h-full flex flex-col my-0 justify-center items-center'>
        <input {...getInputProps()} />
        <p className='text-2xl font-semibold'>Drag and drop your video here.</p>
        <div className='flex justify-center items-align'>
          <button type="button" className='py-2 px-2 text-white text-xl bg-pink-800 cursor-pointer rounded mt-4' onClick={open}>Browse Files</button>
        </div>
      </div>
    </section>
  );
}

Dropzone.propTypes = {
    onFileSelected: PropTypes.func.isRequired,
};

