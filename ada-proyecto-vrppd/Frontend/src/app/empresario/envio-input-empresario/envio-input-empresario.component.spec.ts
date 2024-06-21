import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EnvioInputEmpresarioComponent } from './envio-input-empresario.component';

describe('EnvioInputEmpresarioComponent', () => {
  let component: EnvioInputEmpresarioComponent;
  let fixture: ComponentFixture<EnvioInputEmpresarioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EnvioInputEmpresarioComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EnvioInputEmpresarioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
