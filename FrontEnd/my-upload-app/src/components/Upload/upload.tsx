import React, { useMemo } from 'react'
import Uppy from '@uppy/core'
import type { Uppy as UppyClass } from '@uppy/core'
import XHRUpload from '@uppy/xhr-upload'
import { Dashboard } from '@uppy/react'

import '@uppy/core/css/style.css'
import '@uppy/dashboard/css/style.css'

const Upload: React.FC = () => {
  const uppy = useMemo(() => {
    const instance: UppyClass = new Uppy({
      restrictions: {
        maxFileSize: 5 * 1024 * 1024 * 1024, // 5GB
        allowedFileTypes: ['.csv', '.json', '.xlsx', '.xml'],
      },
      autoProceed: true,
      debug: true,
    })

    instance.use(XHRUpload, {
      endpoint: 'http://localhost:8000/api/v1/uploads/upload-csv',
      method: 'POST',
      fieldName: 'file',
      bundle: false,
      limit: 3,
    })

    return instance
  }, [])

  return (
    <div style={{ maxWidth: '800px', margin: 'auto', padding: '20px' }}>
      <h2>Upload de Arquivos Grandes</h2>
      <Dashboard
        uppy={uppy}
        height={400}
        note="Arraste arquivos ou clique para selecionar"
        proudlyDisplayPoweredByUppy={false}
      />
    </div>
  )
}

export default Upload
