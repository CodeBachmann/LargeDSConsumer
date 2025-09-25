import React, { useEffect } from 'react';
import Uppy from '@uppy/core';
import { DragDrop } from '@uppy/react';
import XHRUpload from '@uppy/xhr-upload';
import '@uppy/core/dist/style.css';
import '@uppy/drag-drop/dist/style.css';

const Upload: React.FC = () => {
  const uppy = Uppy({
    restrictions: {
      maxFileSize: 5 * 1024 * 1024 * 1024, // 5GB máximo, ajuste conforme precisa
      allowedFileTypes: ['.csv', '.json', '.xlsx', '.xml'], // arquivos aceitos
    },
    autoProceed: true, // começa o upload ao escolher arquivo
    debug: true,
  });

  uppy.use(XHRUpload, {
    endpoint: 'http://localhost:8000/upload', // ajuste para seu endpoint FastAPI
    method: 'POST',
    fieldName: 'file',
    bundle: false,
    limit: 3, // uploads paralelos
    headers: {
      // se precisar autenticação, pode colocar aqui
    },
  });

  useEffect(() => {
    return () => uppy.close(); // limpa quando componente desmonta
  }, []);

  return (
    <div style={{ maxWidth: '600px', margin: 'auto', padding: '20px' }}>
      <h2>Upload de Arquivos Grandes</h2>
      <DragDrop
        uppy={uppy}
        locale={{
          strings: {
            // texto no drag and drop
            dropHereOr: 'Arraste arquivos aqui ou clique para selecionar',
          },
        }}
      />
    </div>
  );
};

export default Upload;
